def convert_to_timestamp(text: str) -> str:
    """
    This function takes in text like '11:20' and converts it to a timestamp like '1120000'.
    Handles cases where the text is an empty string.
    """
    milliseconds = 0
    infos = text.split()
    info = infos[0]
    time = info.split(':')
    minutes, seconds = map(int, time)
    timestamp = (minutes * 60) + seconds
    return f"{timestamp}{milliseconds:03d}"

filename = r"C:\Users\aweso\Desktop\conversion\timestamps.txt"
with open(filename) as input_file, open("results.txt", 'w') as output_file:
    for line in input_file.readlines():
        try:
            timestamp = convert_to_timestamp(line.strip())  # Remove leading/trailing whitespaces
            output_file.write(f"{timestamp}\n")
        except ValueError as e:
            print(line, e)
        except IndexError as e:
            #print(line, e)
            pass
            
