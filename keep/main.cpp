#include"nlib.h"
#include"inpnishi.h"

using namespace std;

int quatnishi(Inp_nishi);

int main(int argc, char *argv[]){
   cout<<"Version info. quatnishi v.1.1.0 \n";
// ##################### ARGUMENT HANDLING ##########################
// argv[1]: input parameter file
  if( argv[1]==NULL ){
    puts("No ARGUMEMTS");
    puts("USAGE: ./a.out (argv[1]: input parameter file)" );
    return 1;
  }
  cout<<"Your input-parameter file: "<<argv[1]<<endl;

// INPUT_PARAMETERS
   //Inp_nishi inp1( "parameter.txt" );
   Inp_nishi inp1( argv[1] );
   
// DO quatnishi
   quatnishi(inp1);
  
  if(1==2){}
  else if(1==2){}
  else cout<<"itazura"<<endl;

// END
	cout<<"\nit took "<<(float)clock()/CLOCKS_PER_SEC<<" sec of CPU to execute this program"<<endl;
	return 0;
}
