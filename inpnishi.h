/*  CLASS tra_nishi
*/
#include"nlib.h"

#ifndef _INCLUDE_INPUT_PARAMETERS_
#define _INCLUDE_INPUT_PARAMETERS_
class Inp_nishi{
private:
public:
        //struct inp_se{ int sta_rnum; int end_rnum; string sta_chai; string end_chai; }
        //struct inp_se input;
   string filename;
	
   Inp_nishi( const char *inputname );
   string read( string );
};

/*Inp_nishi::Inp_nishi(const char *inputname){
   filename = inputname;
}*/
#endif


