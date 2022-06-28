import RichTextEditor from "../components/RichTextEditor";
import { TopNavbar } from "../components/TopNavbar";

export const TextEditor = () => {
  return (
    <div className="font-montserrat flex flex-col justify-center items-center">
      <TopNavbar />
      <RichTextEditor />
    </div>
  );
};
