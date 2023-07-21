from pytube import YouTube

def download_video(url, output_path):
    try:
        # Create a YouTube object with the provided URL
        youtube = YouTube(url)

        # Get the first available video stream with the highest resolution
        video = youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        # Download the video to the specified output path
        video.download(output_path)

        print("Video downloaded successfully!")
    except Exception as e:
        print("Error occurred while downloading the video:", str(e))

# Example usage
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
output_directory = "/path/to/save/videos"
download_video(video_url, output_directory)