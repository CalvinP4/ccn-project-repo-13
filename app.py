from flask import Flask, request, render_template, jsonify, send_file
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

input_dir = None

@app.route('/run_model', methods=['POST'])
def run_model():
    global input_dir
    input_video = request.json.get('input_video')
    input_video_name = request.json.get('input_video_name')
    print("input_video_name:", input_video_name)  
    input_dir = os.path.dirname(input_video)

    # Set the input directory
    input_dir = os.path.dirname(input_video)

    # Construct the command
    command = f"python demo.py --input \"{input_video}\" --audio"

    try:
        # Run the command using subprocess
        subprocess.run(command, shell=True, check=True)

        # Paths to the generated video files
        video1_path = os.path.join(input_dir, f"{input_video_name}_shape.mp4")
        video2_path = os.path.join(input_dir, f"{input_video_name}_grid.mp4")

        return jsonify({
            'status': 'success',
            'message': 'Model ran successfully',
            'video1_url': f'/videos/{os.path.basename(video1_path)}',
            'video2_url': f'/videos/{os.path.basename(video2_path)}'
        })
    except subprocess.CalledProcessError as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/videos/<filename>')
def serve_video(filename):
    if input_dir is None:
        return "Error: Input directory is not set. Please run the model first.", 400
    
    video_path = os.path.join(input_dir, filename)
    return send_file(video_path, mimetype='video/mp4')

if __name__ == '__main__':
    app.run(debug=True)
