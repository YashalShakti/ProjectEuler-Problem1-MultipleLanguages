#include <iostream>
#include <list>
using namespace std;
class Euler {
 private:
  int start;
  int end;

 public:
  Euler(int start, int end) {
    this->start = start;
    this->end = end;
  }

  int calculate() {
    int sum = 0;
    list<int> divisors;
    for (int i = start; i < end; i++) {
      if (i % 3 == 0 || i % 5 == 0) {
        divisors.push_back(i);
        sum += i;
      }
    }
    list<int>::iterator i;
    cout << "The divisors are: ";
    for (i = divisors.begin(); i != divisors.end(); i++) {
      cout << *i << " ";
    }
    cout << endl;
    return sum;
  }
};
int main(int argc, char *args[]) {
  int start, end;
  cout << "Enter the start limit : ";
  cin >> start;
  cout << "Enter the end limit : ";
  cin >> end;
  Euler *euler = new Euler(start, end);
  int result = euler->calculate();
  cout << "The result is " << result << endl;
}
