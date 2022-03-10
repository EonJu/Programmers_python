//https://programmers.co.kr/learn/courses/30/lessons/60058
import java.util.Stack;
class Solution {
    
  
    public Boolean IsPerfect(String p)
    {
        Stack<Character> stack = new Stack<>();

        for(int i = 0 ; i<p.length() ; i++)
        {
            if(p.charAt(i) == '(')
            {
                stack.push('(');
            }
            else
            {
                if(stack.isEmpty() == true)
                {
                    return  false;
                }
                stack.pop();
            }
        }

        if(stack.isEmpty() != true)
        {
            return  false;
        }

        return  true;
    }
    public String Recursive(String p)
    {
        if(p.length() == 0)
        {
            return  "";
        }
     
        String u = "";
        String v = "";
        String answer ="";
        int leftCnt = 0;
        int rightCnt = 0;
        int splitNum = 0;

        Stack<Character> stack = new Stack<>();

        for(int i = 0 ; i<p.length() ; i++) {
            if(p.charAt(i) == '(')
            {
                leftCnt ++;
            }
            else
            {
                rightCnt ++;
            }
            if( leftCnt == rightCnt && (leftCnt !=0 && rightCnt !=0) ) {
                //u,v 할당해준다
                u = p.substring(0,i+1);
                if( i != p.length()-1) {
                    v = p.substring(i + 1, p.length());
                }
                break;
            }
        }


        if(IsPerfect(u) == true)
        {
            return  u + Recursive(v);
        }
        else
        {
            answer = "("+Recursive(v);
            answer += ")";
            String temp= u.substring(1,u.length()-1);
            temp = temp.replace("(",".");
            temp = temp.replace(")","(");
            temp = temp.replace(".",")");
            answer +=temp;
            return answer; 
 
        }
    }
    public String solution(String p) {
        String answer = "";
        Boolean bPerfect = IsPerfect(p);
        if(bPerfect == true)
        {
            return p;
        }
        else
        {
            return Recursive(p);
        }
    }
}
