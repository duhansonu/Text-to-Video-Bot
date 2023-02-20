import os
import random
from gtts import gTTS
from moviepy.editor import *
from moviepy.video.tools.credits import credits1
from moviepy.video.tools.subtitles import SubtitlesClip

# Define text-to-speech function
def text_to_speech(text, language='en'):
    tts = gTTS(text, lang=language)
    filename = f"audio_{random.randint(1, 1000000)}.mp3"
    tts.save(filename)
    return filename

# Define video creation function
def text_to_video(text, bg_image, language='en'):
    # Convert text to speech
    audio_file = text_to_speech(text, language=language)
    audio_clip = AudioFileClip(audio_file)
    audio_duration = audio_clip.duration

    #bg_clip = VideoFileClip(bg_image, audio_duration)
    # Set up video clips
    bg_clip = VideoFileClip(bg_image).subclip(0, audio_duration)
    audio_clip = AudioFileClip(audio_file).subclip(0, audio_duration)

    # Add audio clip to background video
    final_clip = bg_clip.set_audio(audio_clip)

    # Create text clip and add it to the final clip
    txt_clip = TextClip(text, fontsize=40, color='white').set_duration(5)
    txt_clip = txt_clip.set_position(('center', 'center'))
    final_clip = CompositeVideoClip([final_clip, txt_clip])

    # Export video and clean up
    video_file = f"video_{random.randint(1, 1000000)}.mp4"
    final_clip.write_videofile(video_file)
    audio_clip.close()  # close the audio file
    os.remove(audio_file)
    return video_file


# Example usage
text = "Hello world!"
bg_image = "background.jpg"
video_file = text_to_video(text, bg_image)
print(f"Video created: {video_file}")
