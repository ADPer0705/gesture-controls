import cv2

class CameraManager:
    """Manages the camera feed."""
    def __init__(self, camera_index=0):
        """Initializes the camera capture object.

        Args:
            camera_index (int): The index of the camera to use (default is 0).
        """
        self.cap = cv2.VideoCapture(camera_index)
        if not self.cap.isOpened():
            raise IOError("Cannot open webcam")

    def get_frame(self):
        """Reads a single frame from the camera.

        Returns:
            tuple: A tuple containing a boolean success flag and the frame.
        """
        success, frame = self.cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            return False, None
        # Flip the frame horizontally for a more intuitive selfie-view
        frame = cv2.flip(frame, 1)
        return True, frame

    def release(self):
        """Releases the camera capture object."""
        self.cap.release()