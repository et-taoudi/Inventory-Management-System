def calculate_checksum(box_ids):
    count_two = 0  # Counter for IDs with exactly two repeated letters
    count_three = 0  # Counter for IDs with exactly three repeated letters
    repeated_letters_two = []  # List to store letters repeated twice
    repeated_letters_three = []  # List to store letters repeated three times

    for box_id in box_ids:
        letter_count = {}  # Dictionary to store the count of each letter in the box ID

        # Count the occurrences of each letter in the box ID
        for letter in box_id:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

        # Check if there are any letters with exactly two or three occurrences
        for letter, count in letter_count.items():
            if count == 2 and letter not in repeated_letters_two:
                count_two += 1
                repeated_letters_two.append(letter)
            elif count == 3 and letter not in repeated_letters_three:
                count_three += 1
                repeated_letters_three.append(letter)

    # Calculate the checksum by multiplying the counts
    checksum = count_two * count_three

    return checksum, count_two, count_three


# Example
box_ids = ["abcdefne", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
checksum = calculate_checksum(box_ids)
print(f"The checksum is: {checksum[0]}")
print(f"The letters repeated 2 times : {checksum[1]}")
print(f"The letters repeated 3 times: {checksum[2]}")

