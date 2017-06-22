public class CheckAvs {

    private static String canonize(String avsNo) {
        return avsNo.replace(".", "");
    }

    public static boolean isValidAvsNumber(String avsNo) {
        avsNo = canonize(avsNo);

        if (avsNo.length() != 13) return false;

        int total = 0;

        for(int i = 0 ; i < 12 ; i+=2) {
            total += digitAt(avsNo, i);
        }

        for(int i = 1 ; i < 12 ; i+=2) {
            total += 3 * digitAt(avsNo, i);
        }

        int actualKey = digitAt(avsNo, 12);
        int expectedKey = 0;

        if (total % 10 != 0) {
            int roundTenUp = (total / 10) * 10 + 10;
            expectedKey = roundTenUp - total;
        }

        return expectedKey == actualKey;
    }

    private static int digitAt(String str, int i) {
        return Integer.parseInt(String.valueOf(str.charAt(i)));
    }

    public static void main(String[] args) {
        String avsNo = args[0];
        System.out.println(isValidAvsNumber(avsNo) ? "Valid" : "Invalid");
    }
}
