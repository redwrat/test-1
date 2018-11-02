#include <iostream>
#include <hello/hello.hpp>

int main()
{
	hello::greetings(std::cout) << std::endl;
	return 0;
}

