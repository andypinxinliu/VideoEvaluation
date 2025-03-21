import json
import os

def generate_html(json_file, output_file, idx):
    # Read the JSON data
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    num_groups = len(data['groups'])
    
    # Start HTML content
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>"""
    
    html_content += data['title'] + """</title>
  <style>
    * {
      box-sizing: border-box;
      font-family: Arial, sans-serif;
    }
    body {
      margin: 0;
      padding: 10px;
    }
    h1 {
      font-size: 1.5rem;
      margin-top: 10px;
    }
    h3 {
      font-size: 1.2rem;
      margin-top: 20px;
      background-color: #f0f0f0;
      padding: 5px;
    }
    .group-container {
      margin-bottom: 20px;
      border: 1px solid #ddd;
      border-radius: 5px;
      padding: 10px;
    }
    .video-container {
      width: 100%;
      margin-bottom: 10px;
    }
    video {
      width: 100%;
      max-height: 300px;
      object-fit: contain;
    }
    .prompt-text {
      margin: 10px 0;
      font-style: italic;
      font-size: 0.9em;
      border-left: 3px solid #ccc;
      padding-left: 10px;
    }
    .metric {
      margin: 15px 0;
      padding: 8px;
      background-color: #f9f9f9;
      border-radius: 4px;
    }
    .metric-title {
      font-weight: bold;
      margin-bottom: 5px;
    }
    .rating {
      display: flex;
      justify-content: space-between;
      width: 100%;
    }
    .rating label {
      flex: 1;
      text-align: center;
      padding: 8px 0;
      border: 1px solid #ddd;
      background-color: #f5f5f5;
      margin: 0 2px;
      border-radius: 4px;
    }
    .rating label:active {
      background-color: #e0e0e0;
    }
    .rating input {
      display: none;
    }
    .rating input:checked + span {
      color: white;
      font-weight: bold;
    }
    .rating label:nth-child(1) input:checked + span { background-color: #ff4d4d; }
    .rating label:nth-child(2) input:checked + span { background-color: #ff9966; }
    .rating label:nth-child(3) input:checked + span { background-color: #ffcc00; }
    .rating label:nth-child(4) input:checked + span { background-color: #99cc33; }
    .rating label:nth-child(5) input:checked + span { background-color: #33cc33; }
    .rating label span {
      display: block;
      padding: 5px 0;
      border-radius: 3px;
    }
    .warning {
      color: red;
      font-size: 0.8em;
      margin-top: 2px;
      display: none;
    }
    .submit-btn {
      background-color: #4CAF50;
      color: white;
      border: none;
      padding: 12px 20px;
      text-align: center;
      text-decoration: none;
      font-size: 16px;
      width: 100%;
      margin: 20px 0;
      border-radius: 5px;
      cursor: pointer;
    }
    #resultOutput {
      width: 100%;
      height: 80px;
      margin: 10px 0;
      padding: 8px;
    }
    /* Hide iframe on mobile */
    @media (max-width: 768px) {
      .google-form-container {
        display: none;
      }
    }
    .action-btn {
      padding: 10px;
      margin: 5px;
      background-color: #f5f5f5;
      border: 1px solid #ddd;
      border-radius: 4px;
      font-size: 14px;
      cursor: pointer;
    }
    .action-btn.primary {
      background-color: #4285F4;
      color: white;
      border: none;
    }
    .success-message {
      color: green;
      font-weight: bold;
      margin: 10px 0;
      display: none;
    }
  </style>
</head>
<body>

  <h1>"""
    
    html_content += data['title'] + """</h1>
  <p>Thank you for participating in the evaluation.</p>
  <p><strong>Instructions</strong>:</p>
  <p>"""
    
    html_content += data['instructions'].replace('\n', '<br>') + """</p>
  
  <form id="evaluationForm">
    <input type="hidden" id="evaluationIdx" value=\"""" + str(idx) + """\">
"""

    # Add each group
    for group_idx, group in enumerate(data['groups']):
        prompt_text = group.get('prompt', 'No prompt available')
        
        group_html = """
    <!-- Group """ + str(group_idx + 1) + """ -->
    <div class="group-container">
      <h3>Group """ + str(group_idx + 1) + """</h3>
      
      <div class="video-container">
        <video controls playsinline>
          <source src=\"""" + group['video'] + """\" type="video/mp4">
          Your browser does not support the video tag.
        </video>
      </div>
      
      <div class="prompt-text">
        <strong>Prompt:</strong> """ + prompt_text + """
      </div>
      
      <div class="metric">
        <div class="metric-title">Prompt Following</div>
        <div class="rating" id="group_""" + str(group_idx + 1) + """_rating_1">
          <label><input type="radio" name="group_""" + str(group_idx + 1) + """_rating_1" value="1"><span>1</span></label>
          <label><input type="radio" name="group_""" + str(group_idx + 1) + """_rating_1" value="2"><span>2</span></label>
          <label><input type="radio" name="group_""" + str(group_idx + 1) + """_rating_1" value="3"><span>3</span></label>
          <label><input type="radio" name="group_""" + str(group_idx + 1) + """_rating_1" value="4"><span>4</span></label>
          <label><input type="radio" name="group_""" + str(group_idx + 1) + """_rating_1" value="5"><span>5</span></label>
        </div>
        <div class="warning" id="warning_group_""" + str(group_idx + 1) + """_rating_1">Please rate this metric</div>
      </div>
      
      <div class="metric">
        <div class="metric-title">Motion Quality</div>
        <div class="rating" id="group_""" + str(group_idx + 1) + """_rating_2">
          <label><input type="radio" name="group_""" + str(group_idx + 1) + """_rating_2" value="1"><span>1</span></label>
          <label><input type="radio" name="group_""" + str(group_idx + 1) + """_rating_2" value="2"><span>2</span></label>
          <label><input type="radio" name="group_""" + str(group_idx + 1) + """_rating_2" value="3"><span>3</span></label>
          <label><input type="radio" name="group_""" + str(group_idx + 1) + """_rating_2" value="4"><span>4</span></label>
          <label><input type="radio" name="group_""" + str(group_idx + 1) + """_rating_2" value="5"><span>5</span></label>
        </div>
        <div class="warning" id="warning_group_""" + str(group_idx + 1) + """_rating_2">Please rate this metric</div>
      </div>
      
      <div class="metric">
        <div class="metric-title">Camera Move</div>
        <div class="rating" id="group_""" + str(group_idx + 1) + """_rating_3">
          <label><input type="radio" name="group_""" + str(group_idx + 1) + """_rating_3" value="1"><span>1</span></label>
          <label><input type="radio" name="group_""" + str(group_idx + 1) + """_rating_3" value="2"><span>2</span></label>
          <label><input type="radio" name="group_""" + str(group_idx + 1) + """_rating_3" value="3"><span>3</span></label>
          <label><input type="radio" name="group_""" + str(group_idx + 1) + """_rating_3" value="4"><span>4</span></label>
          <label><input type="radio" name="group_""" + str(group_idx + 1) + """_rating_3" value="5"><span>5</span></label>
        </div>
        <div class="warning" id="warning_group_""" + str(group_idx + 1) + """_rating_3">Please rate this metric</div>
      </div>
      
      <div class="metric">
        <div class="metric-title">Overall Quality</div>
        <div class="rating" id="group_""" + str(group_idx + 1) + """_rating_4">
          <label><input type="radio" name="group_""" + str(group_idx + 1) + """_rating_4" value="1"><span>1</span></label>
          <label><input type="radio" name="group_""" + str(group_idx + 1) + """_rating_4" value="2"><span>2</span></label>
          <label><input type="radio" name="group_""" + str(group_idx + 1) + """_rating_4" value="3"><span>3</span></label>
          <label><input type="radio" name="group_""" + str(group_idx + 1) + """_rating_4" value="4"><span>4</span></label>
          <label><input type="radio" name="group_""" + str(group_idx + 1) + """_rating_4" value="5"><span>5</span></label>
        </div>
        <div class="warning" id="warning_group_""" + str(group_idx + 1) + """_rating_4">Please rate this metric</div>
      </div>
    </div>
    <!-- End of Group """ + str(group_idx + 1) + """ -->"""
        
        html_content += group_html

    # JavaScript part
    js_part = """
  <button type="submit" class="submit-btn" id="submitButton">Complete Evaluation</button>
  </form>

  <div id="resultContainer" style="display: none; text-align: center; margin-top: 20px;">
    <div id="resultText">
      <p>Your evaluation has been recorded:</p>
      <textarea id="resultOutput" readonly style="margin-bottom: 15px;"></textarea>
    </div>
    
    <button id="submitToGoogleBtn" class="submit-btn" style="background-color: #4285F4;">
      Submit to Google Form
    </button>
    
    <p style="margin-top: 15px; font-size: 0.8em;">
      If the button doesn't work, you can <span id="copyManuallyBtn" style="color: blue; text-decoration: underline;">copy the text</span> 
      and manually <a href="https://forms.gle/Qaj5fN7ENBCjRJkF8" target="_blank">open the form</a>.
    </p>
  </div>
  
  <div class="google-form-container">
    <iframe src="https://forms.gle/hnLC11HCRUSJUHGF7" width="100%" height="450" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
  </div>

  <script>
    // Add touch-friendly behavior for rating selection
    document.querySelectorAll('.rating label').forEach(label => {
      label.addEventListener('click', function() {
        // Remove active class from siblings
        const parent = this.parentNode;
        parent.querySelectorAll('label').forEach(sibling => {
          sibling.querySelector('span').style.backgroundColor = '';
        });
        
        // Add active class to selected
        this.querySelector('span').style.backgroundColor = getColorForValue(this.querySelector('input').value);
        
        // Hide warning if visible
        const warningId = 'warning_' + parent.id;
        document.getElementById(warningId).style.display = 'none';
      });
    });
    
    function getColorForValue(value) {
      const colors = {
        '1': '#ff4d4d',
        '2': '#ff9966',
        '3': '#ffcc00',
        '4': '#99cc33',
        '5': '#33cc33'
      };
      return colors[value] || '';
    }
    
    // Global submit handler function that works on both mobile and desktop
    function handleFormSubmit(e) {
      if (e) {
        e.preventDefault();
        e.stopPropagation();
      }
      
      // Collect evaluation data
      var resultArray = [];
      var evaluationIdx = document.getElementById('evaluationIdx').value;
      var evaluationNumber = "evaluation_" + evaluationIdx;
      resultArray.push(evaluationNumber);

      // Get ratings for each group
      var ratings = [];
      var valid = true;

      for (var i = 1; i <= """ + str(num_groups) + """; i++) {
        var groupName = "group_" + i;
        
        // Get ratings for each metric
        for (var j = 1; j <= 4; j++) {
          var ratingName = groupName + "_rating_" + j;
          var rating = document.querySelector('input[name="' + ratingName + '"]:checked')?.value;
          
          if (!rating) {
            document.getElementById('warning_' + ratingName).style.display = 'block';
            valid = false;
          } else {
            ratings.push(rating);
          }
        }
      }

      if (!valid) {
        alert('Please rate all metrics for all groups');
        return false;
      }

      resultArray.push(ratings.join(","));
      var resultText = resultArray.join(",");
      
      // Store the result text
      document.getElementById('resultOutput').value = resultText;
      
      // IMPORTANT: Show UI feedback immediately
      document.getElementById('loadingMessage').style.display = 'block';
      document.getElementById('loadingMessage').scrollIntoView({behavior: 'smooth'});
      
      // For direct Google Form submission, we'll use a hidden iframe
      try {
        // First create our form-submission iframe if it doesn't exist
        var submissionFrame = document.getElementById('hidden-submission-frame');
        if (!submissionFrame) {
          submissionFrame = document.createElement('iframe');
          submissionFrame.setAttribute('id', 'hidden-submission-frame');
          submissionFrame.setAttribute('name', 'hidden-submission-frame');
          submissionFrame.style.display = 'none';
          document.body.appendChild(submissionFrame);
        }
        
        // Then create a form element we'll submit
        var dynamicForm = document.createElement('form');
        dynamicForm.setAttribute('method', 'post');
        dynamicForm.setAttribute('action', 'https://docs.google.com/forms/d/e/1FAIpQLSfLl5MpC49YvL2ZBAVlbMGslHX4TfWLl3coTSuZr07MN3qrVg/formResponse');
        dynamicForm.setAttribute('target', 'hidden-submission-frame');
        
        // Add our data input field
        var inputField = document.createElement('input');
        inputField.setAttribute('type', 'text');
        inputField.setAttribute('name', 'entry.940024549');
        inputField.setAttribute('value', resultText);
        dynamicForm.appendChild(inputField);
        
        // Add the form to the page, submit it, and remove it
        document.body.appendChild(dynamicForm);
        dynamicForm.submit();
        
        // Show success message after a short delay
        setTimeout(function() {
          document.getElementById('loadingMessage').style.display = 'none';
          document.getElementById('successMessage').style.display = 'block';
          document.getElementById('successMessage').scrollIntoView({behavior: 'smooth'});
          document.getElementById('resultContainer').style.display = 'block';
        }, 2000);
      } 
      catch (error) {
        console.error("Error during submission:", error);
        // Fallback method if iframe submission fails
        submitViaFetch(resultText);
      }
      
      return false;
    }
    
    // Fetch API submission as backup
    function submitViaFetch(resultText) {
      var formData = new FormData();
      formData.append('entry.940024549', resultText);
      
      fetch('https://docs.google.com/forms/d/e/1FAIpQLSfLl5MpC49YvL2ZBAVlbMGslHX4TfWLl3coTSuZr07MN3qrVg/formResponse', {
        method: 'POST',
        mode: 'no-cors',
        body: formData
      })
      .finally(function() {
        // Always show success message after fetch attempt
        document.getElementById('loadingMessage').style.display = 'none';
        document.getElementById('successMessage').style.display = 'block';
        document.getElementById('successMessage').scrollIntoView({behavior: 'smooth'});
        document.getElementById('resultContainer').style.display = 'block';
      });
    }
    
    // Multiple event bindings for better cross-platform compatibility
    
    // 1. Handle button click directly
    document.getElementById('submitButton').addEventListener('click', handleFormSubmit);
    
    // 2. Handle form submission event
    document.getElementById('evaluationForm').addEventListener('submit', handleFormSubmit);
    
    // 3. Backup direct assignment
    document.getElementById('submitButton').onclick = handleFormSubmit;
    
    // Copy data button functionality for backup method
    document.getElementById('copyDataBtn').addEventListener('click', function() {
      var resultOutput = document.getElementById('resultOutput');
      resultOutput.select();
      resultOutput.setSelectionRange(0, 99999); // For mobile devices
      
      navigator.clipboard.writeText(resultOutput.value)
        .then(() => {
          document.getElementById('copySuccess').style.display = 'block';
          this.innerHTML = '✓ COPIED!';
          
          setTimeout(() => {
            this.innerHTML = 'Copy Data';
            document.getElementById('copySuccess').style.display = 'none';
          }, 2000);
        })
        .catch(err => {
          alert('Please manually select and copy the text in the box');
        });
    });
  </script>
  </script>
</body>
</html>"""

    html_content += js_part

    # Write the HTML content to the output file
    with open(output_file, 'w') as file:
        file.write(html_content)

# Example usage
output_dir = 'htmls'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
for json_file in os.listdir('jsons'):
    idx = int(json_file.split('_')[1].split('.')[0])
    generate_html(f'jsons/{json_file}', f'{output_dir}/output_{idx}.html', idx)