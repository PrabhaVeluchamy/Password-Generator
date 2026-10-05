import string
import secrets


def generate_password(length):
    """Generate a secure password containing letters, numbers and symbols."""

    if length < 4:
        raise ValueError("Password length must be at least 4.")

    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    # Guarantee at least one character from each required category
    password = [
        secrets.choice(string.ascii_letters),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]

    # Fill the remaining characters
    for _ in range(length - 3):
        password.append(secrets.choice(characters))

    # Securely shuffle the password
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


def main():
    print("=" * 50)
    print("        SECURE PASSWORD GENERATOR")
    print("=" * 50)

    while True:
        try:
            length = int(input("\nEnter password length (minimum 4): "))

            if length < 4:
                print("❌ Password length must be at least 4.")
                continue

            count = int(input("How many passwords do you want to generate? "))

            if count <= 0:
                print("❌ Number of passwords must be greater than 0.")
                continue

            print("\nGenerated Passwords")
            print("-" * 50)

            for i in range(1, count + 1):
                password = generate_password(length)
                print(f"{i}. {password}")

            print("-" * 50)

            choice = input(
                "\nDo you want to generate more passwords? (y/n): "
            ).lower()

            if choice != "y":
                print("\nThank you for using Secure Password Generator!")
                break

        except ValueError:
            print("❌ Please enter valid numeric values.")


if __name__ == "__main__":
    main()