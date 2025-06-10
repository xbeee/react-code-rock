import axios from "axios";
import React from 'react'
import {Link} from 'react-router-dom'
import AppContext from "../context";

const Header = (props) => {
    const {profileData} = React.useContext(AppContext)
   
    return ( 
        <>
            {profileData.profile_role == 'гость' ?
            (<header>
                 <div>
                    <Link to='/'>
                        <div className="logo">
                            <img src="../img/logo.svg" alt="" />
                        </div>
                    </Link>
                    <Link to='/' className="under aActive">о нас</Link>
                    <Link to='/galary'>каталог</Link>
                </div>
                <div className="noAuth">
                    <Link to='/login'>
                        <a href="">ВХОД</a>
                    </Link>
                    <Link to='/register'>
                        <a href="">РЕГИСТРАЦИЯ</a>
                    </Link>
                </div>
            </header>)
            : profileData.profile_role == 'producer' ? (
                <header>
                    <div>
                        <Link to='/'>
                            <div className="logo">
                                <img src="../img/logo.svg" alt="shop" />
                            </div>
                        </Link>
                        <Link to='/'>о нас</Link>
                        <Link to='/galary'>каталог</Link>
                    </div>
                    <div className="Auth">
                        <span>Привет, продовец!</span>
                        <Link to='/producer'>
                            <img src="../img/shop.svg" alt="shop" />
                        </Link>
                    </div>
                </header>
            ) : (
                <header>
                    <div>
                        <div className="logo">
                            <img src="../img/logo.svg" alt="logotype" />
                        </div>
                        <a href="">о нас</a>
                        <Link to='/galary'>каталог</Link>
                    </div>
                    <div className="Auth">
                        <span>Привет, пользователь!</span>
                        <Link to='/user'>
                            <img src="../img/User.svg" alt="user" />
                        </Link>
                        <a href="">
                            <img src="../img/Cart.svg" alt="cart" />
                        </a>
                    </div>
                    {/* <button onClick={logMeOut}>Выйти</button>
                    <Link to='/galary'>
                        <button>каталог</button>
                    </Link> */}
                 </header>
            )
            }
        </>
     );
}
 
export default Header;