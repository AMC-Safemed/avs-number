//Rextester.Program.Main is the entry point for your code. Don't change it.
//Compiler version 4.0.30319.17929 for Microsoft (R) .NET Framework 4.5

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace Rextester
{
    public class Program
    {
        private static string Canonize(string avsNo)
        {
            return avsNo.Replace(".", "");
        }
        
        private static int GetDigit(string str, int i)
        {
            return str[i] - '0';
        }
        
        public static bool IsValidAvsNumber(string avsNo)
        {
            avsNo = Canonize(avsNo);
            
            if (avsNo.Length != 13) return false;
            
            int total = 0;
            
            for(int i = 0 ; i < 12 ; i += 2) {
                total += GetDigit(avsNo, i);
            }
            
            for(int i = 1 ; i < 12 ; i += 2) {
                total += 3 * GetDigit(avsNo, i);
            }
            
            int expectedKey = 0;
            int actualKey = GetDigit(avsNo, 12);
            
            if (total % 10 != 0) {
                int roundTenUp = (total/10) * 10 + 10;
                expectedKey = roundTenUp - total;
            }
            
            return expectedKey == actualKey;
        }
        
        
        public static void Main(string[] args)
        {
            string avsNo = "756.1234.5678.97";
            Console.WriteLine(IsValidAvsNumber(avsNo) ? "Valid" : "Invalid");
        }
    }
}
