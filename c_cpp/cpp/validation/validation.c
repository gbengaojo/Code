#include <iostream>
#include <string>
#include <limits>

int main() {
    int age;

    std::cout << Enter your age: ;

    if (!(std::cin >> age)) {
        std::cerr << Invalid input.n;
        return 1;
    }

    if (age < 0 || age > 120) {
        std::cerr << Age is out of range.n;
        return 1;
    }

    std::cout << Input accepted.n;
    return 0;
}
