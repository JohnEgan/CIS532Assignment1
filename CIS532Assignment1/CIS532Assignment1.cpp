// CIS532Assignment1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"

#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

std::string GetInput();
std::string * CircularShift(std::string input);

int main()
{

	std::string input;

	input = GetInput();

	CircularShift(input);

	
	std::getline(std::cin, input);

}

std::string GetInput() {

	std::string input;

	std::cout << "Enter in a string: ";
	std::getline(std::cin, input);

	//removes newline character 
	input.erase(std::remove(input.begin(), input.end(), '\n'), input.end());

	return input;

}

std::string * CircularShift(std::string input) {

	int spaces = 0;
	int l = input.length();
	for (int i = 0; i < l; i++) {
		if (input.at(i) == ' ') {
			spaces++;
		}
	}

	std::string rotations = new std::string[spaces];



	return rotations;
}



// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
