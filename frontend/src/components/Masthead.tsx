import MastheadLive from "./MastheadLive";
import styles from "./Masthead.module.css";

const SECTIONS = [
  { href: "#simulasi", label: "Simulasi" },
  { href: "#hemat", label: "Hemat" },
  { href: "#kurva-tidur", label: "Kurva tidur" },
  { href: "#cara-kerja", label: "Cara kerja" },
];

export default function Masthead() {
  return (
    <header className={styles.masthead}>
      <div className="wrap">
        <div className={styles.top}>
          <div>
            <p className={styles.wordmark}>ComfyAir</p>
            <p className={styles.motto}>Setpoint AC dari cuaca di luar</p>
          </div>
          <MastheadLive />
        </div>
        <div className={styles.bar}>
          <nav aria-label="Bagian halaman">
            <ul className={styles.nav}>
              {SECTIONS.map((section) => (
                <li key={section.href}>
                  <a href={section.href}>{section.label}</a>
                </li>
              ))}
            </ul>
          </nav>
          <p className={styles.edition}>Lembar No. 01 · Senior Project TI</p>
        </div>
      </div>
    </header>
  );
}
