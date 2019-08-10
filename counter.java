
import java.util.Random;
 class apples{
	public static void main(String args[])
	{
   Random kobby= new Random ();
   int num;
   for (int counter=0; counter<9; counter++)
   {
   num = 1+kobby.nextInt(6);


     //for (int x :num)

   	System.out.println(num);
   }
   


}

}