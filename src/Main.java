import java.util.*;

public class Main {
    private static class Euler {
        private int start;
        private int end;

        public Euler(int start, int end) {
            this.start = start;
            this.end = end;
        }

        public int calculate() {
            List<Integer> divisors = new ArrayList<>();
            int sum = 0;
            for (int i = start; i < end; i++) {
                if (i % 3 == 0 || i % 5 == 0) {
                    divisors.add(i);
                    sum += i;
                }
            }
            System.out.println("The list of divisors : " + divisors);
            return sum;
        }
    }

    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the start limit :");
        int start = scanner.nextInt();
        System.out.print("Enter the end limit :");
        int end = scanner.nextInt();
        Euler euler = new Euler(start, end);
        int result = euler.calculate();
        System.out.println("The result is " + result);
    }
}