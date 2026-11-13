
# ==========================================
# IRP-II: Task 3
# Runner-up Score
# ==========================================

# Take number of scores

n = int(input("Enter number of scores: "))

# Validate number of scores

if n < 2 or n > 100:
    print("Invalid number of scores.")

else:

    # Take scores from user

    scores = list(
        map(int, input("Enter scores: ").split())
    )

    # Validate input count

    if len(scores) != n:
        print("Please enter exactly", n, "scores.")

    elif any(score < 0 or score > 100 for score in scores):
        print("Scores must be between 0 and 100.")

    else:

        # Remove duplicate scores

        unique_scores = set(scores)

        # Check at least two distinct scores

        if len(unique_scores) < 2:
            print("At least two distinct scores required.")

        else:

            # Remove highest score

            unique_scores.remove(max(unique_scores))

            # Find runner-up score

            runner_up = max(unique_scores)

            print("Runner-up score:", runner_up)
