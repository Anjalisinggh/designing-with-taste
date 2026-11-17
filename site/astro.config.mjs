import { defineConfig } from 'astro/config';

// The site is deployed on Vercel and served from the domain root.
export default defineConfig({
  site: `https://${process.env.VERCEL_PROJECT_PRODUCTION_URL || process.env.VERCEL_URL || 'site-one-umber-77.vercel.app'}`,
  base: '/',
});
