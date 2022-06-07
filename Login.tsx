import { Logo } from "./Logo";

export const Login = () => {
  return (
    <div className="flex flex-col items-center justify-center mt-20">
      <Logo />
      <div className="mt-20">
        <div className="px-5 z-10 h-3">
          <h2 className="text-center bg-white inline-block w-14 font-bold">
            Login
          </h2>
        </div>
        <form
          className="flex flex-col border-2 rounded-md border-teal-600/50 w-80 p-5 h-50 z-0"
          action=""
        >
          <label
            className="flex flex-col text-sm font-montserrat lg:px-2 text-left"
            htmlFor=""
          >
            Email/User
          </label>
          <input
            className="flex flex-col px-3 h-8 bg-teal-600/50 mt-1"
            type="text"
          />

          <label
            className="flex flex-col text-sm font-montserrat lg:px-2 text-left mt-2"
            htmlFor=""
          >
            Contraseñas
          </label>
          <input
            className="flex flex-col px-3 h-8 bg-teal-600/50 mt-1 mb-10"
            type="text"
          />
          <button className="flex flex-col items-center justify-center h-10 px-6 w-70 bg-teal-600 rounded font-semibold text-sm text-white relative">
            Login
          </button>
        </form>
        <h2 className="flex flex-col items-center justify-center mt-20">
          <a className="text-blue-500" href="">
            Te Olvidaste la contraseña?
          </a>
        </h2>
        <h2 className="flex flex-col items-center justify-center mt-10">
          No tienes una cuenta?{" "}
          <a className="text-blue-500" href="">
            Registrate
          </a>
        </h2>
      </div>
    </div>
  );
};
