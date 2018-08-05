package info.androidhive.androidlocation;

import java.util.List;

import okhttp3.RequestBody;
import retrofit2.Call;
import retrofit2.http.GET;

public interface GitHubService {
  @GET("/api")
  Call<User> singleUser();

}