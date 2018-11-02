#include <hello/hello.hpp>

namespace hello {

std::ostream& greetings(std::ostream& stream)
{
    return stream << "Hello, corehard";
}

}
