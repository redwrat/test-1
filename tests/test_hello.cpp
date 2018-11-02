#include <sstream>

#include <gtest/gtest.h>

#include <hello/hello.hpp>

TEST(hello, greetings) {
    std::stringstream ss;
    hello::greetings(ss);
    ASSERT_FALSE(ss.str().empty());
}

