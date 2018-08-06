package info.androidhive.androidlocation;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Query;

public interface GitHubService {
//  @GET("/api")
//  Call<User> singleUser();


  @GET("/api")
  Call<User> singleUser(@Query("latitude") String latitude, @Query("longitude") String longitude);
}