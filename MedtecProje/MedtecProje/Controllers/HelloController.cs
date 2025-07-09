using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace MedtecProje.Controllers
{   
    [Route("api/[controller]")]
    [ApiController]
    public class HelloController : ControllerBase
    {
        [HttpHead]
        public string Get()
        {
            return "Merhaba, Swagger!";
        }
    }
}
