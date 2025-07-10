var builder = WebApplication.CreateBuilder(args);

// Add services to the container.

builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// Configure the HTTP request pipeline. Https ile istek gönderdiğim için doğru olmuyor burası
app.UseSwagger();
app.UseSwaggerUI(c => {
    c.SwaggerEndpoint("/swagger/v1/swagger.json", "My API V1");
    c.RoutePrefix = "swagger"; // Swagger UI'yi kök dizine koyar
});

app.UseHttpsRedirection();

app.UseStaticFiles(); // app.UseSwagger()'dan önce veya sonra olabilir.Sonradan ekledim

app.UseAuthorization();

app.MapControllers();

app.Run();
