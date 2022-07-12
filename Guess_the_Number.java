/* Java Exercise 3: Guess the Number (OOPs Edition)
        Create a class Game, which allows a user to play "Guess the Number" game once.

        Game should have the following methods:
            1. Constructor to generate the random number
            2. takeUserInput() to take a user input of number
            3. isCorrectNumber() to detect whether the number entered by the user is true
            4. getter and setter for noOfGuesses
            5. Use properties such as noOfGuesses(int), etc. to get this task done! */

import java.util.Random;
import java.util.Scanner;

class Game {
    int num, guess, noOfGuesses = 0;

    Game() {
        Random ran = new Random();
        num = ran.nextInt(1, 21);
    }

    void takeUserInput() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Type your choice: ");
        guess = sc.nextInt();
    }

    byte isCorrectNumber(int n) {
        if (n == num)
            return 2;
        else if (n < num)
            return 1;
        else
            return 3;
    }

    void numGuess() {
        noOfGuesses++;
    }
}

public class Guess_the_Number {
    public static void main(String[] args) {
        Game numGame = new Game();

        while (true) {
            numGame.takeUserInput();
            byte res = numGame.isCorrectNumber(numGame.guess);
            numGame.numGuess();

            if (res == 2) {
                System.out.println("\nBingo !!!");
                System.out.println("Guess of Computer: " + numGame.num);
                System.out.println("Your guess: " + numGame.guess);
                System.out.println("Number of guesses you took: " + numGame.noOfGuesses);
                break;
            } else if (res == 1) {
                System.out.println("Your guess: " + numGame.guess);
                System.out.println("Your Number is lesser");
            } else {
                System.out.println("Your guess: " + numGame.guess);
                System.out.println("Your Number is greater");
            }
        }
    }
}
