    import cv2
    import argparse
    import os

    def video_maker(image_folder,video_name = 'video.avi'):
        images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
        frame = cv2.imread(os.path.join(image_folder, images[0]))
        height, width, layers = frame.shape

        video = cv2.VideoWriter(video_name, 0, 1, (width,height))

        for image in images:
            video.write(cv2.imread(os.path.join(image_folder, image)))

        cv2.destroyAllWindows()
        video.release()

    if __name__=='__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument('--image-dir', type=str, default='/dataset/semantic-kitti/00/velodyne/outputs/')
        args = parser.parse_args()
        video_maker(args.image_dir)
             