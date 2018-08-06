package info.androidhive.androidlocation;

public class User {
    String Red_Lights;
    String School_Zone;
    String Speeding;

    @Override
    public String toString() {
        if(Red_Lights == null){
            Red_Lights = "";
        }
        if(School_Zone == null){
            School_Zone = "";
        }
        if(Speeding == null){
            Speeding = "";
        }
        return "Red_Lights: " + Red_Lights + " School_Zone: " + School_Zone + " Speeding: " + Speeding;
    }

    public boolean getSchool(){
        if(School_Zone.charAt(0) == 'T'){
            return true;
        }else{
            return false;
        }
    }

    public int getLight(){
        return Math.round(Float.valueOf(Red_Lights));
    }

    public int getSpeed(){
        return Math.round(Float.valueOf(Speeding));
    }
}
