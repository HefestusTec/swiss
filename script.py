from match_log import MatchLog
import pairing_strategies.min_cost as min_cost


def main():
    ml = MatchLog()
    ml.add_player("Poleto")
    ml.add_player("Freitas")
    ml.add_player("Rafael")
    ml.add_player("Maicon")
    ml.add_player("Guerreiro")
    ml.add_player("Luana")
    ml.add_player("Ana")

    for round in range(1, 4):
        print(f"Round {round}")

        pairings = min_cost.pairings(ml)

        print(f"Bye: {pairings.bye_player}")

        for pairing in pairings.pairs:
            result = input(f"{pairing.player_a} VS. {pairing.player_b}: ")
            result_a, result_b = result.rstrip().split()
            ml.add_result(pairing.player_a, pairing.player_b, result_a, result_b)
        ml.add_bye(pairings.bye_player, 2)

        print("Results:")
        for i, player in enumerate(ml.ranking()[:-1]):
            print(f"{i+1}. {player} ({ml.player_score(player)})")
        print("-" * 20)

    print("Final ranking:")
    for i, player in enumerate(ml.ranking()[:-1]):
        print(f"{i+1}. {player} ({ml.player_score(player)})")


if __name__ == "__main__":
    main()
