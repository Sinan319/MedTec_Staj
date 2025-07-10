using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace MedtecProje.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class LoginController : ControllerBase
    {
        [HttpPost]
        public IActionResult Post([FromBody] LoginModel login)
        {
            if (login.Username == "stajyer" && login.Password == "1234")
            {
                return Ok(new { message = "Giriş başarılı" });
            }
            else
            {
                return Unauthorized(new { message = "Giriş başarısız" });
            }
        }
    }

    public class LoginModel
    {
        public string Username { get; set; } = string.Empty;
        public string Password { get; set; } = string.Empty;
    }
}

