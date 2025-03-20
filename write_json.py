import os
import json
import random

paths_group1 = ['results/luma-raw/videos']
path_group2 = ['results/ours/videos']
path_group3 = ['results/runway-raw/videos']
path_group4 = ['results/w-out-cam-cogvideo/videos']
path_group5 = ['results/w-out-cam-ltx/videos']
path_group6 = ['results/w-out-cam-mochi/videos']
path_group7 = ['results/w-out-cam-wan/videos']
path_group8 = ['results/pika-raw/videos']



# 25 videos from each group, in total 125 videos, if we recruit 20 participants, 
# each watch 20 videos, in total 400 videos, so sample 2 from each group
# there should not be any repeated videos

# Step 2: Distribute videos into sets for participants
num_participants = 20

# Create a list of lists for each participant
participant_sets = {}

# Fill each participant's set
for i in range(num_participants):
    all_sampled_paths = []
    all_sampled_prompts = []

    cur_group_videos = []
    cur_prompt_group = []
    for path in paths_group1:
        # randomly sample 25 videos
        for video in os.listdir(path):
            video_path = os.path.join(path, video)
            cur_group_videos.append(video_path)

    sampled_videos = random.sample(cur_group_videos, 2)
    all_sampled_paths.extend(sampled_videos)


    cur_group_videos = []
    for path in path_group2:
        # randomly sample 25 videos
        for video in os.listdir(path):
            video_path = os.path.join(path, video)
            cur_group_videos.append(video_path)


    sampled_videos = random.sample(cur_group_videos, 2)
    all_sampled_paths.extend(sampled_videos)
    

    cur_group_videos = []
    for path in path_group3:
        # randomly sample 25 videos
        for video in os.listdir(path):
            video_path = os.path.join(path, video)
            cur_group_videos.append(video_path)

    sampled_videos = random.sample(cur_group_videos, 2)
    all_sampled_paths.extend(sampled_videos)
    

    cur_group_videos = []
    for path in path_group4:
        # randomly sample 25 videos
        for video in os.listdir(path):
            video_path = os.path.join(path, video)
            cur_group_videos.append(video_path)
            

    sampled_videos = random.sample(cur_group_videos, 2)
    all_sampled_paths.extend(sampled_videos)

    cur_group_videos = []
    for path in path_group5:
        # randomly sample 25 videos
        for video in os.listdir(path):
            video_path = os.path.join(path, video)
            cur_group_videos.append(video_path)

    sampled_videos = random.sample(cur_group_videos, 2)
    all_sampled_paths.extend(sampled_videos)
    
    
    
    cur_group_videos = []
    for path in path_group6:
        # randomly sample 25 videos
        for video in os.listdir(path):
            video_path = os.path.join(path, video)
            cur_group_videos.append(video_path)

    sampled_videos = random.sample(cur_group_videos, 2)
    all_sampled_paths.extend(sampled_videos)
    
    
    
    cur_group_videos = []
    for path in path_group7:
        # randomly sample 25 videos
        for video in os.listdir(path):
            video_path = os.path.join(path, video)
            cur_group_videos.append(video_path)

    sampled_videos = random.sample(cur_group_videos, 2)
    all_sampled_paths.extend(sampled_videos)


    cur_group_videos = []
    for path in path_group8:
        # randomly sample 25 videos
        for video in os.listdir(path):
            video_path = os.path.join(path, video)
            cur_group_videos.append(video_path)

    sampled_videos = random.sample(cur_group_videos, 2)
    all_sampled_paths.extend(sampled_videos)

    # Shuffle the complete list of sampled videos
    random.shuffle(all_sampled_paths)
    all_sampled_prompts = [sampled_path.replace('.mp4', '.txt').replace('videos', 'prompts') for sampled_path in all_sampled_paths]

    participant_sets[i] = (all_sampled_paths, all_sampled_prompts)

json_path = 'jsons'
if not os.path.exists(json_path):
    os.makedirs(json_path)

# Step 3: Write the participant sets to a JSON file
json_base = {
    "title": "Subjective Evaluation of Video Generation Quality",

    "instructions": "Please watch each video and rate the videos based on Four evaluation metrics,\n \
        1. Prompt following: How well does the video follow the prompt\n \
        2. Motion Quality: Whether the motion in the video is smooth and natural\n \
        3. Camera Move: Whether the video present the camera move in a natural way\n \
        4. Overall: Overall quality of the video\n \
    Please rate each video on a scale of 1 to 5, where 1 is the lowest and 5 is the highest\n",

    "groups":[]
}

for i, participant_set in participant_sets.items():
    
    cur_json = json_base.copy()
    for video_path, prompt_path in zip(participant_set[0], participant_set[1]):

        # read the prompt file
        with open(prompt_path, 'r') as f:
            prompt = f.read()
        
        
        id_name = None
        if 'luma-raw' in video_path:
            id_name = 'luma-raw'
        elif 'ours' in video_path:
            id_name = 'ours'
        elif 'runway-raw' in video_path:
            id_name = 'runway-raw'
        elif 'w-out-cam-cogvideo' in video_path:
            id_name = 'w-out-cam-cogvideo'
        elif 'w-out-cam-ltx' in video_path:
            id_name = 'w-out-cam-ltx'
        elif 'w-out-cam-mochi' in video_path: 
            id_name = 'w-out-cam-mochi'
        elif 'w-out-cam-wan' in video_path:
            id_name = 'w-out-cam-wan'
        elif 'pika-raw' in video_path:
            id_name = 'pika-raw'
        else:
            raise ValueError(f"Unknown video path: {video_path}")

        video_path = '../' + video_path
        group = {
            "sample_id": id_name,
            "prompt": prompt,
            "video": video_path,
            "captions": [ 
            # Prompt following
            "1. Very poor: Does not follow the prompt at all\n\
            2. Poor: Barely follows the prompt\n\
            3. Fair: Somewhat follows the prompt\n\
            4. Good: Mostly follows the prompt\n\
            5. Excellent: Perfectly follows the prompt\n",
            # Motion quality
            "1. Very poor: Motion is extremely choppy\n\
            2. Poor: Motion is not smooth\n\
            3. Fair: Motion is somewhat smooth\n\
            4. Good: Motion is smooth but not flawless\n\
            5. Excellent: Motion is perfectly smooth\n",
            # Camera move
            "1. Very poor: Camera movement is unnatural\n\
            2. Poor: Camera movement is awkward\n\
            3. Fair: Camera movement is acceptable\n\
            4. Good: Camera movement is natural but not perfect\n\
            5. Excellent: Camera movement is perfectly natural\n",
            # Overall
            "1. Very poor: Overall quality is unacceptable\n\
            2. Poor: Overall quality is below average\n\
            3. Fair: Overall quality is average\n\
            4. Good: Overall quality is above average\n\
            5. Excellent: Overall quality is outstanding\n",
            ],
        }
        cur_json["groups"].append(group)
    
    # save the json file
    with open(f'{json_path}/participant_{i+1}.json', 'w') as f:
        json.dump(cur_json, f, indent=4)
        print(f'Participant {i+1} JSON file saved')
    

