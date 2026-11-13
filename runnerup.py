# Runner-up Score Problem

def find_runner_up(scores):

    unique_scores = set(scores)

    if len(unique_scores) < 2:
        return None

    unique_scores.remove(max(unique_scores))

    return max(unique_scores)


# Main program

n = int(input("Enter number of scores: "))

if 2 <= n <= 100:

    scores = list(map(int, input("Enter scores: ").split()))

    if len(scores) != n:
        print("Please enter exactly", n, "scores.")

    elif any(score < 0 or score > 100 for score in scores):
        print("Invalid scores.")

    else:
        result = find_runner_up(scores)

        if result is None:
            print("Two distinct scores are required.")
        else:
            print("Runner-up score:", result)

else:
    print("Invalid number of scores.")