import json

def generate_html(json_file, output_file, idx):
    # Read the JSON data
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    num_groups = len(data['groups'])
    
    # Start HTML content
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{data['title']}</title>
  <style>
    table img {{
      width: 100%;
      max-width: 300px;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
    }}
    table, th, td {{
      border: 1px solid black;
    }}
    th, td {{
      padding: 10px;
      text-align: center; /* Center-align text and images */
    }}
    .rating {{
      display: flex;
      justify-content: center;
      gap: 10px;
    }}
    .warning {{
      color: red;
      font-weight: bold;
      display: none;
    }}
  </style>
</head>
<body>

<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src=""></script>
<script>
  window.dataLayer = window.dataLayer || [];

  function gtag() {{
    dataLayer.push(arguments);
  }}

  gtag('js', new Date());

  gtag('config', '');
</script>

<section>
  <div>
    <h1>{data['title']}</h1>
    <p>Thank you for participating in the subjective evaluation.</p>
    <p><strong>Instructions (测试说明)</strong>: </p>
    <p>{data['instructions']}</p>
    <br>
    <form id="evaluationForm">
      <input type="hidden" id="evaluationIdx" value="{idx}">"""

    # Add each group
    for idx, group in enumerate(data['groups']):
        html_content += f"""
      <!-- Group {idx + 1} -->
      <h3>Group {idx + 1}</h3>
      <div></div>
      <div>
        <table style="table-layout: fixed;">
          <col span="1" style="width: 25%;">
          <col span="1" style="width: 25%;">
          <col span="1" style="width: 25%;">
          <col span="1" style="width: 25%;">
          <thead>
            <tr>
              <th style="text-align: center">Reference</th>
              <th style="text-align: center">Test Sample 1</th>
              <th style="text-align: center">Test Sample 2</th>
              <th style="text-align: center">Test Sample 3</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="text-align: center">
                <img src="{group['image']}" alt="Reference Image">
              </td>
              <td style="text-align: center">
                {group['captions'][0]}
                <div class="rating" id="group_{idx + 1}_rating_1">
                  <label><input type="radio" name="group_{idx + 1}_rating_1" value="1"> 1</label>
                  <label><input type="radio" name="group_{idx + 1}_rating_1" value="2"> 2</label>
                  <label><input type="radio" name="group_{idx + 1}_rating_1" value="3"> 3</label>
                  <label><input type="radio" name="group_{idx + 1}_rating_1" value="4"> 4</label>
                  <label><input type="radio" name="group_{idx + 1}_rating_1" value="5"> 5</label>
                  <label><input type="radio" name="group_{idx + 1}_rating_1" value="6"> 6</label>
                  <label><input type="radio" name="group_{idx + 1}_rating_1" value="7"> 7</label>
                  <label><input type="radio" name="group_{idx + 1}_rating_1" value="8"> 8</label>
                  <label><input type="radio" name="group_{idx + 1}_rating_1" value="9"> 9</label>
                  <label><input type="radio" name="group_{idx + 1}_rating_1" value="10"> 10</label>
                </div>
                <div class="warning" id="warning_group_{idx + 1}_rating_1">Please rate this caption.</div>
              </td>
              <td style="text-align: center">
                {group['captions'][1]}
                <div class="rating" id="group_{idx + 1}_rating_2">
                  <label><input type="radio" name="group_{idx + 1}_rating_2" value="1"> 1</label>
                  <label><input type="radio" name="group_{idx + 1}_rating_2" value="2"> 2</label>
                  <label><input type="radio" name="group_{idx + 1}_rating_2" value="3"> 3</label>
                  <label><input type="radio" name="group_{idx + 1}_rating_2" value="4"> 4</label>
                  <label><input type="radio" name="group_{idx + 1}_rating_2" value="5"> 5</label>
                  <label><input type="radio" name="group_{idx + 1}_rating_2" value="6"> 6</label>
                  <label><input type="radio" name="group_{idx + 1}_rating_2" value="7"> 7</label>
                  <label><input type="radio" name="group_{idx + 1}_rating_2" value="8"> 8</label>
                  <label><input type="radio" name="group_{idx + 1}_rating_2" value="9"> 9</label>
                  <label><input type="radio" name="group_{idx + 1}_rating_2" value="10"> 10</label>
                </div>
                <div class="warning" id="warning_group_{idx + 1}_rating_2">Please rate this caption.</div>
              </td>
              <td style="text-align: center">
                {group['captions'][2]}
                <div class="rating" id="group_{idx + 1}_rating_3">
                  <label><input type="radio" name="group_{idx + 1}_rating_3" value="1"> 1</label>
                  <label><input type="radio" name="group_{idx + 1}_rating_3" value="2"> 2</label>
                  <label><input type="radio" name="group_{idx + 1}_rating_3" value="3"> 3</label>
                  <label><input type="radio" name="group_{idx + 1}_rating_3" value="4"> 4</label>
                  <label><input type="radio" name="group_{idx + 1}_rating_3" value="5"> 5</label>
                  <label><input type="radio" name="group_{idx + 1}_rating_3" value="6"> 6</label>
                  <label><input type="radio" name="group_{idx + 1}_rating_3" value="7"> 7</label>
                  <label><input type="radio" name="group_{idx + 1}_rating_3" value="8"> 8</label>
                  <label><input type="radio" name="group_{idx + 1}_rating_3" value="9"> 9</label>
                  <label><input type="radio" name="group_{idx + 1}_rating_3" value="10"> 10</label>
                </div>
                <div class="warning" id="warning_group_{idx + 1}_rating_3">Please rate this caption.</div>
              </td>
            </tr>
            <tr>
              <td>&#128204; Which captions sample (Sample 1, Sample 2, Sample 3) is the best description of the target image?</td>
              <td style="text-align: center;">
                <input type="radio" id="group_{idx + 1}_choice_1" name="group_{idx + 1}" value="1" required>
                <label for="group_{idx + 1}_choice_1">This one is most similar to reference</label>
              </td>
              <td style="text-align: center;">
                <input type="radio" id="group_{idx + 1}_choice_2" name="group_{idx + 1}" value="2" required>
                <label for="group_{idx + 1}_choice_2">This one is most similar to reference</label>
              </td>
              <td style="text-align: center;">
                <input type="radio" id="group_{idx + 1}_choice_3" name="group_{idx + 1}" value="3" required>
                <label for="group_{idx + 1}_choice_3">This one is most similar to reference</label>
              </td>
            </tr>"""

        # Add hidden inputs for caption sources
        for i, source in enumerate(group['caption_source']):
            html_content += f'<input type="hidden" id="group_{idx + 1}_source_{i + 1}" value="{source}">'
        cur_sample_id = group['sample_id']
        html_content += f'<input type="hidden" id="group_{idx + 1}_sample_id_{i + 1}" value="{cur_sample_id}">'

        html_content += f"""
          </tbody>
        </table>
      </div>
      <!-- End of Group {idx + 1}. -->"""

    # Add the closing HTML content
    html_content += f"""
      <br><br>
      <!-- Submit button -->
      <div style="text-align: center;">
        <input type="submit" value="Complete" style="width: 150px; height: 50px;">
      </div>
    </form>

    <div id="resultText" style="text-align: center; display: none;">
      <p>Please copy the following text and paste it into Google Forms(请复制以下文本并粘贴到Google Forms中):</p>
      <textarea id="resultOutput"></textarea>
    </div>
    <div style="display: flex; justify-content: center; margin-top: 20px;">
      <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSdmhewMD3r9gd-RxRqe8Ef2Wy5okpzLVzoPXJ9SPrUL5YlLQg/viewform?usp=sf_link" width="640" height="451" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
    </div>
  </section>
</div>
<script>
  document.getElementById('evaluationForm').onsubmit = function(event) {{
      event.preventDefault(); // Prevent form from submitting

      var resultArray = [];
      var currentTime = new Date().toISOString();
      var evaluationIdx = document.getElementById('evaluationIdx').value; // Get evaluation_idx from hidden input
      var evaluationNumber = "evaluation_" + evaluationIdx; // Construct evaluation number using evaluation_idx

      resultArray.push(evaluationNumber);

      // Get user selection for each group
      var choices = [];
      var sources = [];
      var ratings = [];
      var sample_ids = [];
      var valid = true;

      for (var i = 1; i <= {num_groups}; i++) {{
          var groupName = "group_" + i;
          var selectedValue = document.querySelector('input[name="' + groupName + '"]:checked')?.value;
          choices.push(selectedValue || "N/A");

          // Add image path and corresponding source
          if (selectedValue) {{
              sources.push(document.querySelector('#' + groupName + '_source_' + selectedValue).value);
          }} else {{
              sources.push("N/A");
          }}

          // Get sample_id for each group
          // var cur_sample_id = document.querySelector('#' + groupName + '_sample_id_' + selectedValue).value;
          // sample_ids.push(document.querySelector('#' + groupName + '_sample_id_' + selectedValue).value);

          // Get ratings for each caption
          for (var j = 1; j <= 3; j++) {{
              var rating = document.querySelector('input[name="' + groupName + '_rating_' + j + '"]:checked')?.value;
              if (!rating) {{
                  document.getElementById('warning_' + groupName + '_rating_' + j).style.display = 'block';
                  valid = false;
              }} else {{
                  document.getElementById('warning_' + groupName + '_rating_' + j).style.display = 'none';
                  ratings.push(rating);
              }}
          }}
      }}

      if (!valid) {{
          alert('Please rate all captions.');
          return;
      }}

      // resultArray.push(sample_ids.join(","));
      resultArray.push(choices.join(","));
      resultArray.push(sources.join(","));
      resultArray.push(ratings.join(","));

      // Show result text and fill textarea
      var resultText = resultArray.join(",");
      var resultOutput = document.getElementById('resultOutput');
      resultOutput.textContent = resultText;
      resultOutput.style.width = '80%';  // Set the width to 80%
      resultOutput.style.height = '200px';  // Set the height to 200px
      document.getElementById('resultText').style.display = 'block';
  }};
</script>
</body>
</html>"""

    # Write the HTML content to the output file
    with open(output_file, 'w') as file:
        file.write(html_content)

# # Example usage
# generate_html('input.json', 'output.html')
