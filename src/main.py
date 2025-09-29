import cv2
from camera_manager import CameraManager

def main():
    """The main function to run the gesture control application."""
    cam = CameraManager()

    while True:
        # Get a frame from the camera
        success, frame = cam.get_frame()
        if not success:
            break

        # Display the frame
        cv2.imshow('Jarvis Kinetic Controls', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean up
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()