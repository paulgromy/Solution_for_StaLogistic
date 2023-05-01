import uuid
import time
from pathlib import Path
from publisher import publisher


def repeat_every_five_seconds():
    # I check if there is such a folder in the current directory.
    # If not, then create
    Path("data").mkdir(parents=True, exist_ok=True)

    # Code logic: since the file is generated every 5 seconds and the program runtime is 2 minutes,
    # I create a counter that will increase by one every five seconds,
    # and also run the publisher() function every 15 seconds
    count = 0
    while count != 14:
        count += 1
        random_name_for_file = str(uuid.uuid4())  # Create a random filename
        with open("data/" + random_name_for_file, "w") as file:
            file.write(random_name_for_file)
        time.sleep(5)
        if not count % 3:
            publisher()
