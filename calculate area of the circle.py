#include <iostream>
#define phi 22 / 7
//calculate the area of ​​a circle #define
using namespace std;
int main ()
{
    int r;
    float luas;

    cout<<"radius circle : ";
    cin>>r;

//radius process
    luas=phi*r*r;
    cout<<"the area of ​​the circle is "<<luas;
    return 0;
}
