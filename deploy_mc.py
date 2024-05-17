
import subprocess

def get_ml_output():
    try:
        # Run the c that executes your machine learning model
        process = subprocess.Popen(['edge-impulse-linux-runner'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, _ = process.communicate()

        # Decode the output and return the result
        return float(output.decode().strip())

    except Exception as e:
        print(f"Error getting machine learning output: {e}")
        return None

def main():
    # Get the output from the machine learning model
    ml_output = get_ml_output()
    print(ml_output)

    if ml_output is not None:
        # Determine whether it indicates calm or distress based on confidence level
        result = "Calm" if ml_output < 0.5 else "Distress"

        print(f"Model Output: {ml_output}")
        print(f"Situation: {result}")
    else:
        print("Failed to get machine learning output.")

if __name__ == "__main__":
    main()