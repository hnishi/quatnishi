#include"nlib.h"
#include"inpnishi.h"

struct inp_se{ vector<double> ax;vector<double> ay; int iii;};
   //struct inp_se vec_quat;

inp_se ttt( inp_se tttt){
   cout<<"tttt.iii = "<<tttt.iii<<endl;
   tttt.iii ++ ;
   return tttt;
}

int calc( Inp_nishi inp1 ){
   cout<<"Program calc() starts!!!\n";

   inp_se ttttt;
   ttttt.iii = 114;
   cout<<"ttt(ttttt).iii = "<<ttt(ttttt).iii<<endl;;
   
   vector<int> v1;
   v1.push_back(11);v1.push_back(12);
   cout<<v1.size()<<endl;
   vector<int> v2(1);
   v1 = v2;
   cout<<v1.size()<<endl;
	
   cout<<"input file name: "<<inp1.filename<<endl;	
   string test_int;
   test_int = inp1.read("TEST");
   cout<<"inp1.read(\"TEST\"): "<<test_int<<endl;
   int test_int2 = atoi( test_int.c_str() );
   cout<<"atoi of test_int.c_str(): "<<test_int2<<endl;

   test_int = inp1.read("hahaha");
   cout<<"inp1.read(\"hahaha\"): "<<test_int<<endl;
   test_int2 = atoi( test_int.c_str() );
   cout<<"atoi of test_int.c_str(): "<<test_int2<<endl;

   cout<<"chain space \""<<inp1.read("CHAINNAME")<<"\" \n";
// OUTPUT TRAJECTORIES IN MD0
	/*string codname1, pdbname1, outname1;
	char bfcod[200], bfpdb[200], bfout[200];
	
	char buf[3];
	for(int i=1;i<9;i++){
	pdbname1="/Users/nishigami/AbModeling/02mcmd_ab10/cargo_md0/10_npt_43000.pdb";
	codname1="/Users/nishigami/AbModeling/02mcmd_ab10/cargo_md0/no/md0.crd";
	outname1="/Users/nishigami/AbModeling/02mcmd_ab10/cargo_md0/cod150_no.pdb";
	//outname1="cod150_no.pdb";
	//cout<<codname1<<endl;
	//itoa(i,buf,10);
	sprintf(buf,"%d",i);
	codname1.insert(52,buf); //insert "1" behind charcter at 52 in codname1; that is "o" 
	outname1.insert(59,buf);
	//outname1.insert(9,"1");
	
	cout<<codname1<<endl;
	cout<<outname1<<endl;
	strcpy(bfpdb,pdbname1.c_str());
	strcpy(bfcod,codname1.c_str());
	strcpy(bfout,outname1.c_str());
	//cout<<bfpdb<<" "<<bfcod<<endl;
	//tra_nishi tra1(codname1,pdbname1);
	tra_nishi tra1(bfcod,bfpdb);
	tra1.write_cod(bfout,10);
	//tra1.write_cod("zzz.pdb",10);
	}*/
	return 0;
}
