import { ComfortProvider } from "@/components/ComfortProvider";
import Masthead from "@/components/Masthead";
import ComfortExperience from "@/components/ComfortExperience";
import SleepCurve from "@/components/SleepCurve";
import HowItWorks from "@/components/HowItWorks";
import Colophon from "@/components/Colophon";

export default function Home() {
  return (
    <ComfortProvider>
      <a className="skip-link" href="#simulasi">
        Langsung ke simulasi
      </a>
      <Masthead />
      <main id="isi">
        <ComfortExperience />
        <SleepCurve />
        <HowItWorks />
      </main>
      <Colophon />
    </ComfortProvider>
  );
}
