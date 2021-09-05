#include <iostream>
#define phi 22 / 7
//calculate the area of ​​a circle #define
using namespace std;
int main ()
{
    int r;
    float area;

    cout<<"radius circle : ";
    cin>>r;

//radius process
    area=phi*r*r;
    cout<<"the area of ​​the circle is "<<area;
    return 0;
}
