import random

# Niveau 1 – Paiements Blind
blind_payouts = {
    "Quinte royale": 500,
    "Quinte flush": 50,
    "Carré": 10,
    "Full": 3,
    "Couleur": 1.5,
    "Quinte": 1,
    "Brelan": 0,
    "Pair ou moins": 0
}

# Niveau 2 – Paiements Bonus
bonus_payouts = {
    "Quinte royale": 50,
    "Quinte flush": 40,
    "Carré": 30,
    "Full": 8,
    "Couleur": 7,
    "Quinte": 4,
    "Brelan": 3,
    "Pair ou moins": 0
}


def ask_question(level):
    if level == 1:
        payouts = blind_payouts
        mise = "Blind"
        hand = random.choice(list(payouts.keys()))
        correct_answer = payouts[hand]

        try:
            user_input = input(f"Pour une main '{hand}', combien de fois la mise {mise} est payée ? : ")
            user_answer = float(user_input)

            if user_answer == correct_answer:
                print("Bonne réponse !\n")
            else:
                print(f"Mauvaise réponse. La bonne réponse était : {correct_answer}\n")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.\n")

    elif level == 2:
        payouts = bonus_payouts
        mise = "Bonus"
        hand = random.choice(list(payouts.keys()))
        correct_answer = payouts[hand]

        try:
            user_input = input(f"Pour une main '{hand}', combien de fois la mise {mise} est payée ? : ")
            user_answer = float(user_input)

            if user_answer == correct_answer:
                print("Bonne réponse !\n")
            else:
                print(f"Mauvaise réponse. La bonne réponse était : {correct_answer}\n")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.\n")

    elif level == 3:
        # Choisir aléatoirement entre niveau 1 et 2
        if random.choice([True, False]):
            ask_question(1)
        else:
            ask_question(2)

    elif level == 4:
        all_hands = set(blind_payouts.keys()).union(bonus_payouts.keys())
        hand = random.choice(list(all_hands))
        blind_gain = blind_payouts.get(hand, "Aucun")
        bonus_gain = bonus_payouts.get(hand, "Aucun")

        print(f"Main : '{hand}'")
        try:
            user_blind = input("Combien de fois la mise Blind est payée ? : ")
            user_bonus = input("Combien de fois la mise Bonus est payée ? : ")

            blind_user_answer = float(user_blind)
            bonus_user_answer = float(user_bonus)

            blind_correct = (blind_user_answer == blind_gain)
            bonus_correct = (bonus_user_answer == bonus_gain)

            if blind_correct:
                print("Blind : Bonne réponse !")
            else:
                print(f"Blind : Mauvaise réponse. La bonne réponse était : {blind_gain}")

            if bonus_correct:
                print("Bonus : Bonne réponse !\n")
            else:
                print(f"Bonus : Mauvaise réponse. La bonne réponse était : {bonus_gain}\n")

        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.\n")

    else:
        print("Niveau invalide.")


def main():
    print("Quiz Paiements Ultimate Texas Hold'em\n")
    print("Niveaux disponibles :")
    print("1 - Paiement Blind")
    print("2 - Paiement Bonus")
    print("3 - Mix aléatoire des deux")
    print("4 - Les deux en même temps\n")

    level = input("Choisis ton niveau (1, 2, 3 ou 4) : ")
    if level not in ['1', '2', '3', '4']:
        print("Choix invalide. Fin du programme.")
        return

    level = int(level)

    print("\nDébut du quiz ! Tu vas recevoir jusqu’à 100 questions.")
    print("Appuie sur Ctrl+C pour arrêter à tout moment.\n")

    try:
        for i in range(100):
            print(f"Question {i + 1} sur 100")
            ask_question(level)
    except KeyboardInterrupt:
        print("\nQuiz interrompu. À bientôt et bon entraînement !")


if __name__ == "__main__":
    main()
