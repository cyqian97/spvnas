import cv2
import argparse
import os

def video_maker(image_folder,video_name = 'video.mp4'):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images.sort()
    # print(images)
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    video = cv2.VideoWriter(video_name, fourcc, 10, (width,height))
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--image-dir', type=str, default='/dataset/semantic-kitti/00/velodyne/outputs/')
    args = parser.parse_args()
    video_maker(args.image_dir)
             