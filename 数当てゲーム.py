import random





def main():

    print("1～100の数当てゲームを始めます。")

    print("コンピューターが1～100の間の数字を1つ選びました。")

    print("その数字を当ててください。")



    answer = random.randint(1, 100)

    attempts = 0



    while True:

        user_input = input("あなたの予想を入力してください（1～100）：")



        # 数値チェック

        if not user_input.isdigit():

            print("数字を入力してください。")

            continue



        guess = int(user_input)



        if guess < 1 or guess > 100:

            print("1～100の範囲で入力してください。")

            continue



        attempts += 1



        if guess < answer:

            print("もっと大きいです。")

            diff = answer - guess

            if diff <= 2:

                print("惜しい！あと少しで正解です。")

            elif diff >= 10:

                print("全然違います。")

        elif guess > answer:

            print("もっと小さいです。")

            diff = guess - answer

            if diff <= 2:

                print("惜しい！あと少しで正解です。")

            elif diff >= 10:

                print("全然違います。")

        else:

            print(f"正解です！答えは {answer} でした。")

            print(f"あなたの試行回数は {attempts} 回です。")

            break





if __name__ == "__main__":

    main()
    