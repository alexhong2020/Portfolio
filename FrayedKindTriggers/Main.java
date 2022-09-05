import java.util.Scanner;
class Main {
  public static void main(String[] args) {
    //System.out.println("Hello world!");
    Scanner input = new Scanner(System.in);

    System.out.println("Insert length building: ");
    int length = input.nextInt();

    System.out.println("Insert width building: ");
    int width = input.nextInt();

    double calc1;    //Calc if lxl and wxw
    double calc1a;   // l/l
    double calc1b;   // w/w
    int calc1int;

    double calc2;    //Calc if lxw and wxl
    double calc2a;   // l/w
    double calc2b;   // w/l
    int calc2int;
    double l = 5.5;  //Length of 217W solar panel in ft
    double w = 3.25; //Width of 217W solar panel in ft


    calc1a = length/l;
    calc1b = width/w;
    calc1 = calc1a*calc1b;
    calc1int = (int)calc1;

    calc2a = length/w;
    calc2b = width/l;
    calc2 = calc2a*calc2b;
    calc2int = (int)calc2;

    if (calc1int > calc2int){
      System.out.println(calc1int + " solar panels");
    }
    else{
      System.out.println(calc2int + " solar panels");
    }
  }
}