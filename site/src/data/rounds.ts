// Real outputs from the skill's eval runs (iteration 1): same prompt, with and without the skill.
export interface Sample {
  img: string;
  alt: string;
  note: string;
}
export interface Round {
  id: 'chai' | 'gym';
  label: string;
  next: string;
  prompt: string;
  with: Sample;
  without: Sample;
}

export const rounds: Round[] = [
  {
    id: 'chai',
    label: 'Round 1: a chai stall',
    next: 'Try round 2: the gym front desk',
    prompt:
      "make a landing page for my chai tapri 'Tapri No. 7' near FC Road, Pune. cutting chai Rs 15, bun maska Rs 30, poha Rs 40, open 6am to 11pm, insta @taprino7",
    with: {
      img: 'img/chai-with.png',
      alt: 'A yellow painted tin signboard on a green wall reading Tapri No. 7, with the menu and prices painted in red.',
      note: '<strong>Made with the skill.</strong> A painted tin signboard nailed to a wall. Sign lettering, red only on prices, an "open now" board that swings once. It made up nothing it was not told.',
    },
    without: {
      img: 'img/chai-without.png',
      alt: 'A cream page with a large high-contrast serif title, rust accents and small typewriter labels.',
      note: '<strong>Made without it.</strong> Cream ground, high-contrast serif, rust accent, typewriter labels: the look agents reach for once they avoid purple. It also invented ingredients, a neighbourhood and a founding line.',
    },
  },
  {
    id: 'gym',
    label: 'Round 2: a gym front desk',
    next: 'Try round 1: the chai stall',
    prompt:
      "build an admin dashboard for my small gym 'Iron Akhada' so the front desk can see today's check-ins, memberships expiring this week, and pending payments. use sample data for 25 members",
    with: {
      img: 'img/gym-with.png',
      alt: 'A calm dashboard on a cool white ground with blue bars for hourly check-ins and red amounts for fees pending.',
      note: '<strong>Made with the skill.</strong> Dials set to calm and dense. Status colours come from weight plates: red 25 kg for money owed, yellow 15 kg for expiring, green 10 kg for on the floor. Sample data is labelled.',
    },
    without: {
      img: 'img/gym-without.png',
      alt: 'A cream dashboard with terracotta numbers and tracked all-caps section headings.',
      note: '<strong>Made without it.</strong> Cream and terracotta again, tracked all-caps section labels, and nothing on screen says the members are fake.',
    },
  },
];
