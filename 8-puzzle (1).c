#include <stdio.h>
#include <stdlib.h>

#define N 3

#define MAX_DEPTH 50

int grid[N][N] = { {8,0,6}, {5,4,7}, {2,3,1} };
int goal[N][N] = { {0,1,2}, {3,4,5}, {6,7,8} };

int moves[MAX_DEPTH];

int best_moves[MAX_DEPTH];

int best_depth = MAX_DEPTH; 

int isCorrect(){
	int i,j;
	for (i=0;i<N;i++){
		for(j=0;j<N;j++){
			if(grid[i][j]!=goal[i][j]){
				return 0;
			}
		}
	}
	return 1;
}

void search_dfs(int zero_x, int zero_y, int depth, int played_x, int played_y){
	
	if(depth>=best_depth){
		return;
	}
	
	if(depth!=0){
		moves[depth-1]=grid[played_x][played_y];
	}
	
	if(isCorrect() == 1){
		printf("Solution found witch %d steps \n",depth);
		best_depth=depth;
		int i;
		for(i=0;i<depth;i++) {
			best_moves[i]=moves[i];
		}
		return;
	}
	
	int x1,y1;
	int x2,y2;
	int x3,y3;
	int x4,y4;
	
	x1=zero_x+1;
	y1=zero_y;
	
	x2=zero_x-1;
	y2=zero_y;
	
	x3=zero_x;
	y3=zero_y+1;
	
	x4=zero_x;
	y4=zero_y-1;

	// printf("x1=%d, y1=%d, x2=%d, y2=%d, x3=%d, y3=%d, x4=%d, y4=%d,\n", x1, y1, x2, y2, x3, y3, x4, y4);
	
	if(x1==played_x && y1==played_y){
		x1=y1=-1;
	}
	
	if(x2==played_x && y2==played_y) {
		x2=y2=-1;
	}
	
	if(x3==played_x && y3==played_y){
		x3=y3=-1;
	}
	if(x4==played_x && y4==played_y){
		x4=y4=-1;
	}
		
	
	if( (x1>=0) && (y1>=0) && (x1<N) && (y1<N) ){
		grid[zero_x][zero_y]=grid[x1][y1]; grid[x1][y1]=0;
		search_dfs(x1,y1, depth+1, zero_x,zero_y);
		grid[x1][y1]=grid[zero_x][zero_y];grid[zero_x][zero_y]=0;
	}
	
	if( (x2>=0) && (y2>=0) && (x2<N) && (y2<N) ){
		grid[zero_x][zero_y]=grid[x2][y2]; grid[x2][y2]=0;
		search_dfs(x2,y2,depth+1,zero_x,zero_y);
		grid[x2][y2]=grid[zero_x][zero_y];grid[zero_x][zero_y]=0;
	}
	
	if( (x3>=0) && (y3>=0) && (x3<N) && (y3<N) ){
		grid[zero_x][zero_y]=grid[x3][y3]; grid[x3][y3]=0;
		search_dfs(x3,y3,depth+1,zero_x,zero_y);
		grid[x3][y3]=grid[zero_x][zero_y];grid[zero_x][zero_y]=0;
	}
	
	if( (x4>=0) && (y4>=0) && (x4<N) && (y4<N) ){
		grid[zero_x][zero_y]=grid[x4][y4]; grid[x4][y4]=0;
		search_dfs(x4,y4,depth+1,zero_x,zero_y);
		grid[x4][y4]=grid[zero_x][zero_y];grid[zero_x][zero_y]=0;
	}
	
	
}

int main(){
	printf("Puzzle-8 !\n");
	int i,j;
	int origin_x,origin_Y;
	for (i=0;i<N;i++){
		for(j=0;j<N;j++){
			if(grid[i][j]==0){
				origin_x=i;
				origin_Y=j;
				break;
			}
		}
	}	

	 search_dfs(origin_x,origin_Y, 0, -1, -1);
	 
	 for(i=0;i<best_depth;i++)printf("move [%d]=%d\n",i,best_moves[i]);
	 
	 return 0;
}
