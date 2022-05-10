import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
return lst.__len__()
)");
        REQUIRE(ret == 1);
    }

    SECTION("dict.update(dict) [also has __copy__]")
    {
        OPT_TEST_EQUAL("dict(__copy__ = {'a': 1, 2: None}, __deepcopy__ = {'b': 3}).update({2: 2})", "{'a': 1, 2: 2, 'b': 3}");
    }
    SECTION("list.insert(i, 1) [also has __copy__]")
    {
        OPT_TEST_EQUAL("list(__copy__ = [0, 1, 2], __deepcopy__ = [3, 4]).insert(1, 1)", "[0, 1, 1, 2, 3, 4]");
    }
    SECTION("list.extend([1, 2]) [also has __copy__]")
    {
        OPT_TEST_EQUAL("list(__copy__ = [0, 1, 2], __deepcopy__ = [3,
