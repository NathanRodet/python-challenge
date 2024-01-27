from collections import OrderedDict

# Create an ordered hashmap from the provided list of words and return it
def create_ordered_hashmap(file_path):
    ordered_hashmap = OrderedDict()

    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                if len(words) >= 2:
                    key = int(words[0])
                    value = ' '.join(words[1:])
                    ordered_hashmap[key] = value
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

    sorted_hashmap = OrderedDict(sorted(ordered_hashmap.items()))

    return sorted_hashmap

# Create a staircase from the keys of the ordered hashmap return it
def create_staircase(keys):
    subsets = []
    step = 1

    while len(keys) != 0:
        if len(keys) >= step:
            subsets.append(keys[:step])
            keys = keys[step:]
            step += 1
        else:
            return False

    return subsets

# Decode the message reading the last element of each sub-array of the staircase
# and matching it with his value in the ordered hashmap then return the decoded message as an array
def decode_message(ordered_hashmap, staircase):
    values_array = []

    for sub_array in staircase:
        if len(sub_array) == 1:
            key = sub_array[0]
        elif len(sub_array) > 1:
            key = sub_array[-1]
        else:
            print("Invalid sub-array found")
            continue

        if key in ordered_hashmap:
            value = ordered_hashmap[key]
            values_array.append(value)
        else:
            print(f"Key {key} not found in the ordered hashmap.")

    return values_array

def main():
    message_file = "words.txt"
    ordered_hashmap = create_ordered_hashmap(message_file)
    if ordered_hashmap is not None:
        keys = list(ordered_hashmap.keys())
        staircase = create_staircase(keys)
        if staircase is not None:
            decoded_message = decode_message(ordered_hashmap, staircase)
            if decoded_message is not None:
                result = ' '.join(decoded_message)
                print(f"Decoded Message: {result}")

if __name__ == "__main__":
    main()