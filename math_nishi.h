#include"nlib.h"
#include<cmath>
#include<vector>
using namespace std;

/*#ifndef _INCLUDE_AVE_
#define _INCLUDE_AVE_
        inline double ave(float *all, int i){         // to determine averagei
                float total=0;
                int u;
                for(u=0;u<i;u++){
                        total+=all[u];
                }
                return total/i;
        }
#endif*/

#ifndef _INCLUDE_RMSD_
#define _INCLUDE_RMSD_
inline double rmsd(vector<double> &ax,vector<double> &ay,vector<double> &az,
		vector<double> &bx,vector<double> &by,vector<double> &bz) // to calculate R.M.S.D.
{
	double rmsd,tot_x=0,tot_y=0,tot_z=0;
	//double sum=0;
    //printf("debug: size %10d\n",ax.size() );
	if(ax.size() != bx.size() || ax.size() != ay.size() || ay.size() != bz.size() ){
		cerr<<"ERROR: both structures should have the same num. of atoms\n";
		return -1;
	}
	for(unsigned int u=0;u<ax.size();u++){
		tot_x += ( ax[u]- bx[u])*( ax[u]- bx[u]);
		tot_y += ( ay[u]- by[u])*( ay[u]- by[u]);
		tot_z += ( az[u]- bz[u])*( az[u]- bz[u]);
	}
	//sum = tot_x + tot_y + tot_z;
	rmsd=sqrt((tot_x + tot_y + tot_z)/ ax.size());
        return rmsd;
}
#endif
