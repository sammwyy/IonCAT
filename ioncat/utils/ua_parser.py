import random
import logger

UAS = []

# Load UAs from file
def load_uas(path: str):
    try:
        with open(path, "r") as f:
            # Read file
            data = f.read() 
            # Parse file
            lines = data.split("\n")
            # Iterate over lines
            for line in lines:
                # Check if line is not empty
                if line and not line.strip().startswith("#"):
                    # Append line to UAS
                    UAS.append(line)
    except FileNotFoundError:
        logger.warn(f"File not found: {path}")
        logger.warn("IonCAT will run without User-Agents. If you want to use User-Agents, specify a valid file using --uas flag.")
        exit(1) 
                    
# Check if UAs are loaded
def is_uas_loaded():
    return len(UAS) > 0 

# Return random UA
def get_random_ua():
    if not is_uas_loaded():
        return ""
    
    return random.choice(UAS)